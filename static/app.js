const hero= document.querySelector(".hero");
const slider= document.querySelector(".slider");
const headline= document.querySelector(".headline");
const time= document.querySelector(".time");
const raffle= document.querySelector(".raffle");
const winner= document.querySelector(".winner");
const congrats= document.querySelector(".congrats");
const going= document.querySelector(".going");
const c1= document.querySelector(".contestant1");
const c2= document.querySelector(".contestant2");
const c3= document.querySelector(".contestant3");
const c4= document.querySelector(".contestant4");
const c5= document.querySelector(".contestant5");
const c6= document.querySelector(".contestant6");
const c7= document.querySelector(".contestant7");

const tl = new TimelineMax();

//intro slider of image
tl.fromTo(hero, 1, {height: "0%"}, {height: "100%", ease: Power2.easeInOut})
.fromTo(hero, 1.2, {width: '90%'}, {width: '100%', ease: Power2.easeInOut})
.fromTo(slider, 1.2, {y: "-100%"}, {y: "0%", ease: Power2.easeInOut}, "-=1.2")
//contestants into position
.to(c1, {opacity:0, y:'520%', duration: 0})
.to(c2, {opacity:0, y:'520%', duration: 0})
.to(winner, {opacity:0, y:'520%', duration: 0})
.to(c3, {opacity:0, y:'520%', duration: 0})
.to(c4, {opacity:0, y:'520%', duration: 0})
.to(c5, {opacity:0, y:'520%', duration: 0})
.to(c6, {opacity:0, y:'520%', duration: 0})
.to(c7, {opacity:0, y:'520%', duration: 0})
.to(congrats, {opacity:0, y:'520%', duration: 0})
.to(going, {opacity:0, y:'610%', duration: 0})

.fromTo(headline, 0.5, {opacity:0, x: 30}, {opacity:1, x:-125}, "-=.75")

.fromTo(time, 0.5, {opacity:0, x: 30}, {opacity:1, x:-50}, "-=.90")
.to(time, {opacity: 0, duration: 3}, "+=13") // should be .to(time, {opacity: 0, duration: 3}, "+=13")
.fromTo(raffle, .5, {opacity:0, x: -75}, {opacity:1, x:-152}, "-=1")


//slot machine raffle animation
.fromTo(c1, .05, {opacity:0}, {opacity:1})
.fromTo(c1, .05, {opacity:1}, {opacity:0})
.fromTo(c2, .05, {opacity:0}, {opacity:1})
.fromTo(c2, .05, {opacity:1}, {opacity:0})
.fromTo(c3, .05, {opacity:0}, {opacity:1})
.fromTo(c3, .05, {opacity:1}, {opacity:0})
.fromTo(c4, .05, {opacity:0}, {opacity:1})
.fromTo(c4, .05, {opacity:1}, {opacity:0})
.fromTo(c5, .05, {opacity:0}, {opacity:1})
.fromTo(c5, .05, {opacity:1}, {opacity:0})
.fromTo(c6, .05, {opacity:0}, {opacity:1})
.fromTo(c6, .05, {opacity:1}, {opacity:0})
.fromTo(c7, .05, {opacity:0}, {opacity:1})
.fromTo(c7, .05, {opacity:1}, {opacity:0})
.fromTo(c1, .05, {opacity:0}, {opacity:1})
.fromTo(c1, .05, {opacity:1}, {opacity:0})
.fromTo(c2, .05, {opacity:0}, {opacity:1})
.fromTo(c2, .05, {opacity:1}, {opacity:0})
.fromTo(c3, .05, {opacity:0}, {opacity:1})
.fromTo(c3, .05, {opacity:1}, {opacity:0})
.fromTo(c4, .05, {opacity:0}, {opacity:1})
.fromTo(c4, .05, {opacity:1}, {opacity:0})
.fromTo(c5, .05, {opacity:0}, {opacity:1})
.fromTo(c5, .05, {opacity:1}, {opacity:0})
.fromTo(c6, .05, {opacity:0}, {opacity:1})
.fromTo(c6, .05, {opacity:1}, {opacity:0})
.fromTo(c7, .05, {opacity:0}, {opacity:1})
.fromTo(c7, .05, {opacity:1}, {opacity:0})
.fromTo(c1, .05, {opacity:0}, {opacity:1})
.fromTo(c1, .05, {opacity:1}, {opacity:0})
.fromTo(c2, .05, {opacity:0}, {opacity:1})
.fromTo(c2, .05, {opacity:1}, {opacity:0})
.fromTo(c3, .05, {opacity:0}, {opacity:1})
.fromTo(c3, .05, {opacity:1}, {opacity:0})
.fromTo(c4, .05, {opacity:0}, {opacity:1})
.fromTo(c4, .05, {opacity:1}, {opacity:0})
.fromTo(c5, .05, {opacity:0}, {opacity:1})
.fromTo(c5, .05, {opacity:1}, {opacity:0})
.fromTo(c6, .05, {opacity:0}, {opacity:1})
.fromTo(c6, .05, {opacity:1}, {opacity:0})
.fromTo(c7, .05, {opacity:0}, {opacity:1})
.fromTo(c7, .05, {opacity:1}, {opacity:0})
.fromTo(c1, .05, {opacity:0}, {opacity:1})
.fromTo(c1, .05, {opacity:1}, {opacity:0})
.fromTo(c2, .05, {opacity:0}, {opacity:1})
.fromTo(c2, .05, {opacity:1}, {opacity:0})
.fromTo(c3, .05, {opacity:0}, {opacity:1})
.fromTo(c3, .05, {opacity:1}, {opacity:0})
.fromTo(c4, .05, {opacity:0}, {opacity:1})
.fromTo(c4, .05, {opacity:1}, {opacity:0})
.fromTo(c5, .05, {opacity:0}, {opacity:1})
.fromTo(c5, .05, {opacity:1}, {opacity:0})
.fromTo(c6, .05, {opacity:0}, {opacity:1})
.fromTo(c6, .05, {opacity:1}, {opacity:0})
.fromTo(c7, .05, {opacity:0}, {opacity:1})
.fromTo(c7, .05, {opacity:1}, {opacity:0})
.fromTo(winner, 2, {opacity:0}, {opacity:1, ease: Power2.easeInOut})


.to(raffle, {opacity: 0, duration: 2}, "+=3")
.fromTo(winner, 1, {x: -75}, {y: 275, x:-195, ease: Power2.easeInOut}, "-=1")
.fromTo(congrats, 0, {x: -45}, {x:-195, ease: Power2.easeInOut}, "-=1")
.to(congrats, {y:"630%", duration: 0})
.to(congrats, {opacity:1, duration: 2})
.to(going, {opacity:1, duration: 1})












