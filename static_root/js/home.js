function lerp(a,p,b){

	var delta = b-a;
	return a+(p*delta);

}


class OrbitGraphic {
	constructor() {
		this.colour = "#fff";
		this.svg = document.querySelector(".zdog-svg");
		this.canvas = document.querySelector(".zdog-canvas");
		this.frameTime = 1000 / 5;
		this.lastTime = 0;
		this.targetRotation = new Vec2(0,0);
		this.illo = new Zdog.Illustration({
			element: ".zdog-svg",
			dragRotate: true,
			resize: true,
			zoom:this.getZoom(this.svg),
			rotate: { x: 0.86, y: 0.68 },
			translate:{ x:0.5 }
		});
		this.scene = new Zdog.Anchor({
			addTo: this.illo
			//translate: { y: this.svg.clientHeight/2, x:this.svg.clientWidth/2 }
		});
		this.orbit = new Zdog.Anchor({
			addTo: this.scene
		});

		var gapAngle = Zdog.TAU / 10;
		var orbitLineStrokeWidth = 0.015;
		new Zdog.Ellipse({
			addTo: this.orbit,
			diameter: 1,
			quarters: 2,
			stroke: orbitLineStrokeWidth,
			rotate: { z: gapAngle / 2 },
			color: this.colour
		});
		new Zdog.Ellipse({
			addTo: this.orbit,
			diameter: 1,
			quarters: 2,
			stroke: orbitLineStrokeWidth,
			rotate: { z: Zdog.TAU / 2 - gapAngle / 2 },
			color: this.colour
		});
		var pStroke = 0.1;
		var planetPadding = 0.5;
		
		
		let planet = new Zdog.Anchor({
			addTo: this.orbit,
			translate: { y: -0.5 },
			/*stroke: pStroke,
			color: this.colour*/
		});
		new Zdog.Hemisphere({
		  addTo: planet,
		  diameter: pStroke,
		  // fill enabled by default
		  // disable stroke for crisp edge
			rotate:{x:-Math.PI/2},
		  stroke: false,
			color: this.colour,
		  //backface: '#43188a',
		});
		new Zdog.Hemisphere({
		  addTo: planet,
		  diameter: pStroke-0.001,
		  // fill enabled by default
		  // disable stroke for crisp edge
			rotate:{x:Math.PI/2},
		  stroke: false,
			//color: this.colour,
		  color: '#43188a',
		});
		/*new Zdog.Hemisphere({
			addTo: planet,
			diameter:pStroke/10,
			translate: { y: -0.5 },
			color: this.colour,
			backface:"#000"
		});*/

		new Zdog.Shape({
			addTo: this.orbit,
			stroke: 0.2,

			color: this.colour
		});
		
		this.orbit.rotate.z=-1;
		
		window.addEventListener("resize", () => {
			this.onResize();
		});
		
		this.prevScrollHeightSinceLastMouseMove = 0;
		this.mousePos = new Vec2({x:0,y:0});
		document.body.addEventListener("mousemove",(e)=>{
			this.prevScrollHeightSinceLastMouseMove = document.documentElement.scrollTop;
			this.mousePos = new Vec2(e.pageX,e.pageY);
			this.onMouseMove(this.mousePos);
		});
		
		document.addEventListener("scroll",()=>{
			//Deal with scroll events not triggering mouse move.
			var delta = document.documentElement.scrollTop - this.prevScrollHeightSinceLastMouseMove;
			if(delta!=0){
				var vec = this.mousePos.clone();
				vec.y+=delta;
				this.onMouseMove(vec);
			}
		});
	}
	onResize() {
		this.illo.zoom = this.getZoom(this.illo.element);
	}
	getZoom(renderElement){
		return Math.min(
			renderElement.parentElement.offsetWidth,
			renderElement.parentElement.offsetHeight
		) * 0.8;
	}
	update(deltaT) {
		var rotationSpeed = 0.8;
		this.orbit.rotate.z -= (deltaT / 1000) * rotationSpeed;
		var currentRot = new Vec2(this.scene.rotate);
		var lerped = new Vec2(lerp(currentRot.x,0.1,this.targetRotation.x),lerp(currentRot.y,0.1,this.targetRotation.y));
		this.scene.rotate = {x:lerped.x,y:lerped.y};		
	}
	render(delta) {
		this.onResize();
		this.update(delta);
		this.illo.updateRenderGraph();
	}
	onMouseMove(relMousePos){
		var center = new Vec2(this.illo.element.parentElement.offsetWidth/2,this.illo.element.parentElement.offsetHeight/2);
		var deltaCenter = relMousePos.add(center.times(-1));
		deltaCenter = deltaCenter.times(1/this.getZoom(this.illo.element)).times(2);//-1 to 1 ish
		deltaCenter = deltaCenter.times(0.1);
		deltaCenter = deltaCenter.timesComponentwise(new Vec2(-1,1));
		this.targetRotation = deltaCenter;
		
	}
}

var g = new OrbitGraphic();

function loop(t) {
	g.render(1);
	requestAnimationFrame((t) => {
		loop(t);
	}, 1000 / 24);
}

loop(0);
// Cards JS

