#Update for clock project

Updated project version: https://editor.p5js.org/4everstandup/full/E7h0DHa0t

put this source code into p5js environment to make it work. 
 
Source code:


var col1 = {
  r1: 0,
  g1: 0,
  b1: 225
};


function setup() {
  createCanvas(1000, 1000);
  angleMode(DEGREES);
  extraCanvas = createGraphics(1000, 1000);
  extraCanvas.clear();
}

function draw() {
  background(0);
  let hours = hour();
  let mins = minute();
  let secs = second();
  console.log(hours, mins, secs);
  translate(width / 2, height / 2);
  rotate(-90);

  strokeWeight(30);
  stroke(0, 0, 250);
  noFill();
  let secsDegree = map(secs, 0, 60, 0, 360);
  arc(0, 0, 500, 500, 0, secsDegree);

  push();
  rotate(secsDegree);
  line(0, 0, 300, 0);
  pop();

  strokeWeight(25);
  stroke(0, 250,0);
  noFill();
  let minsDegree = map(mins, 0, 60, 0, 360);
  arc(0, 0, 400, 400, 0, minsDegree);

  push();
  rotate(minsDegree);
  line(0, 0, 250, 0);
  pop();

  strokeWeight(23);
  stroke(250,0,0);
  noFill();
  let hoursDegree = map(hours, 0, 60, 0, 360);
  arc(0, 0, 300, 300, 0, hoursDegree);

  push();
  rotate(hoursDegree);
  line(0, 0, 200, 0);
  pop();

  col1.r1 = random(100, 200);
  col1.g1 = random(50, 200);
  col1.b1 = random(0, 225);


  extraCanvas.fill(col1.r1, col1.g1, col1.b1);
  extraCanvas.noStroke();
  extraCanvas.rect(480, 470, 50, 50, 100);

  image(extraCanvas, -500, -500);

}
