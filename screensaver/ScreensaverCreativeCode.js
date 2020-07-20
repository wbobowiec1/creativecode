

var col = {
  r: 255,
  g: 0,
  b: 0
};

var col1 = {
  r1: 0,
  g1: 0,
  b1: 225
};

var spot = {
  x: 100,
  y: 50
};

function setup() {
  createCanvas(800, 600);
  extraCanvas = createGraphics(800, 600);
  extraCanvas.clear();
  background(0);
}

function draw() {


  col.r = random(4, 1);
  col.g = 0;
  col.b = random(1, 225);

  spot.x = random(width);
  spot.y = random(height);
  noStroke();
  fill(col.r, col.g, col.b, 400);
  ellipse(spot.x, spot.y, 50, 1);

  
    col1.r1 = random(60, 225);
  col1.g1 = 0;
  col1.b1 = random(200, 225);
  
  extraCanvas.fill(col1.r1,col1.g1, col1.b1);
  extraCanvas.noStroke();
  let starX = random(width);
  let starY = random(height);
  extraCanvas.rect(starX, starY, 10, 10);

  image(extraCanvas, 0, 0);

}
