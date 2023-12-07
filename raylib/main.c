#include <raylib.h>
#include <stdio.h>
#include <stdlib.h>

#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 450
#define MID_WIDTH 400
#define MID_HEIGHT 225
#define NODE_WIDTH 20

struct Array {
  int length;
  int capacity;
  Vector2 *node;
};

struct Array *initArray(int capacity) {
  struct Array *array = (struct Array *)malloc(sizeof(struct Array));
  array->capacity = capacity;
  array->node = (Vector2 *)malloc(sizeof(Vector2) * capacity);
  array->length = 0;
  return array;
}

Vector2 *createVec2(int x, int y) {
  Vector2 *vec = (Vector2 *)malloc(sizeof(Vector2));
  vec->x = x;
  vec->y = y;
  return vec;
}

struct Array *sailor() {
  int size = 5;
  int coords[5][2] = {{0, 0}, {1, 0}, {0, -1}, {-1, 1}, {-1, -1}};
  struct Array *array = initArray(size);
  for (int i = 0; i < size; i++) {
    array->node[i] = *createVec2(coords[i][0], coords[i][1]);
    array->length++;
  }

  return array;
}
struct Array *stick() {
  int size = 3;
  int coords[3][2] = {{0, 0}, {0, -1}, {0, -2}};
  struct Array *array = initArray(size);

  for (int i = 0; i < size; i++) {
    array->node[i] = *createVec2(coords[i][0], coords[i][1]);
    array->length++;
  }

  return array;
}

struct Array *spaceship() {
  int size = 9;
  int coords[9][2] = {{0, 0},  {1, 0},  {2, 0},   {3, 0},  {3, -1},
                       {3, -2}, {2, -3}, {-1, -1}, {-1, -3}};
  struct Array *array = initArray(size);

  for (int i = 0; i < size; i++) {
    array->node[i] = *createVec2(coords[i][0], coords[i][1]);
    array->length++;
  }

  return array;
}

void drawNodes(struct Array *array) {
  for (int i = 0; i < array->length; i++) {
    Vector2 node = array->node[i];
    int x = MID_WIDTH + node.x * NODE_WIDTH;
    int y = MID_HEIGHT + node.y * NODE_WIDTH;
    DrawRectangle(x, y, NODE_WIDTH, NODE_WIDTH, BLUE);
  }
}

void appendNode(struct Array *array, int x, int y) {
  Vector2 *vec = createVec2(x, y);
  if (array->length >= array->capacity) {
    array->capacity *= 2;
    array->node =
        (Vector2 *)realloc(array->node, array->capacity * sizeof(Vector2));
  }
  array->node[array->length++] = *vec;
}

bool inArray(struct Array *array, int x, int y) {
  for (int i = 0; i < array->length; ++i) {
    Vector2 node = array->node[i];
    if (node.x == x && node.y == y) {
      return true;
    }
  }
  return false;
}

int getNumberOfNeighbours(struct Array *array, int x, int y) {
  int neighbours = 0;
  for (int i = 0; i < array->length; ++i) {
    Vector2 node = array->node[i];
    if (node.x == x && node.y == y) {
      continue;
    }
    if (abs((int)node.x - x) <= 1 && abs((int)node.y - y) <= 1) {
      neighbours++;
    }
  }

  return neighbours;
}

bool nodeBecomesAlive(struct Array *array, int x, int y) {
  return getNumberOfNeighbours(array, x, y) == 3 ? true : false;
}
bool nodeDies(struct Array *array, int x, int y) {
  int neighbours = getNumberOfNeighbours(array, x, y);
  if (neighbours == 2 || neighbours == 3) {
    return false;
  }
  return true;
}

struct Array *getNeighbours(Vector2 node) {
  struct Array *array = initArray(8);
  int coords[8][2] = {{1, 0}, {-1, 0}, {0, 1},  {0, -1},
                      {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
  for (int i = 0; i < 8; i++) {
    appendNode(array, node.x + coords[i][0], node.y + coords[i][1]);
  }

  return array;
}

void updateNodes(struct Array *array) {
  // Get possible new nodes
  // Figure out which becomes alive
  struct Array *newNodes = initArray(8);
  for (int i = 0; i < array->length; ++i) {
    struct Array *neighbours = getNeighbours(array->node[i]);
    for (int j = 0; j < neighbours->length; j++) {

      Vector2 node = neighbours->node[j];
      if (nodeBecomesAlive(array, node.x, node.y) &&
          !inArray(array, node.x, node.y) &&
          !inArray(newNodes, node.x, node.y)) {
        appendNode(newNodes, node.x, node.y);
      }
    }

    // Figure out which dies
    int x = array->node[i].x, y = array->node[i].y;
    if (!nodeDies(array, x, y) && !inArray(newNodes, x, y)) {
      appendNode(newNodes, x, y);
    }
    free(neighbours);
  }
  for (int i = 0; i < newNodes->length; ++i) {
  }
  free(array->node);
  array->node = newNodes->node;
  array->length = newNodes->length;
  array->capacity = newNodes->capacity;
  free(newNodes);
}

int main() {

  char *file_path = "./music/EQ.mp3";

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT,
             "raylib [core] example - basic window");

  struct Array *array = spaceship();
  SetTargetFPS(60);

  // Main game loop
  while (!WindowShouldClose()) // Detect window close button or ESC key
  {
    // Update

    updateNodes(array);
    WaitTime(0.5);
    // Draw
    //----------------------------------------------------------------------------------
    BeginDrawing();
    ClearBackground(RAYWHITE);
    drawNodes(array);

    EndDrawing();
    //----------------------------------------------------------------------------------
  }

  // De-Initialization
  //--------------------------------------------------------------------------------------
  CloseWindow(); // Close window and OpenGL context
  //--------------------------------------------------------------------------------------orld\n");
}
