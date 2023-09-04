

#include <qt5/QtCore/QTimer>
#include <qt5/QtGui/QColor>
#include <qt5/QtWidgets/QtWidgets>

#include <QApplication>
#include <qt5/QtWidgets/qdrawutil.h>
#include <vector>

typedef struct Point {
  int x;
  int y;
} Point;

std::vector<Point> getPossible(std::vector<Point> blocks) { return blocks; }
std::vector<Point> checkDead(std::vector<Point> possibleBlocks,
                             std::vector<Point> blocks) {
  return blocks;
}
std::vector<Point> checkAlive(std::vector<Point> possibleBlocks,
                              std::vector<Point> blocks) {
  return blocks;
}
std::vector<Point> centerBlocks(std::vector<Point> blocks, h, w) {
  return blocks;
}

class MyWidget : public QWidget {
public:
  QTimer *timer;
  MyWidget(QWidget *parent = nullptr) : QWidget(parent) {

    gray = QColor(128, 128, 128);
    black = QColor(0, 0, 0);

    timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(cycle()));

    this->setStyleSheet("background-color: gray;"));
    timer->start(200);
  }

private:
  std::vector<Point> blocks;
  std::vector<Point> oldBlocks;
  QColor gray;
  QColor black;

  void paintEvent(QPaintEvent *) override {

    painter = QPainter(this);
    painter.setPen(gray);
    painter.setBrush(gray);
    for (int i = 0; i < oldBlocks.size(); i++) {
      painter.drawRect(oldBlocks[i].x, oldBlocks[1].y, 20, 20);
    }

    painter.setPen(black);
    painter.setBrush(black);
    for (int i = 0; i < blocks.size(); i++) {
      painter.drawRect(blocks[i].x, blocks[1].y, 20, 20);
    }
  }

private slots:
  void cycle() {
    oldBlocks = blocks;
    std::vector<Point> possibleBlocks = getPossible();
    blocks = checkDead(possibleBlocks, blocks) + checkAlive(blocks, blocks);

    blocks = centerBlocks(blocks, 720, 1280);
    update();
  }
};

int main(int argc, char *argv[]) {
  QApplication app(argc, argv);

  MyWidget widget;
  widget.resize(1280, 720);
  widget.show();

  return app.exec();
}
