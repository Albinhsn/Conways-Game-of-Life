FILES = main.c

LIBS = -I. -L. -lraylib -lglfw3 -lGL -lopenal -lm -lpthread -ldl -lX11 -lXrandr -lXinerama -lXi -lXxf86vm -lXcursor

b:
	gcc -o main  $(FILES) $(LIBS)

r:
	gcc -o main $(FILES) $(LIBS) && ./main
