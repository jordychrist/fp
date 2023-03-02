const tl = gsap.timeline({defaults: {ease: 'power1.out'}})

tl.to('.text', {y:'0%', duration: 2, stagger: .90});
tl.to('.slider', {y: "-100%", duration: 1.5, delay: 0.9});
tl.to('.intro', {y: "-100%", duration: 1 }, "-=1");
tl.fromTo('nav', {opacity: 0}, {opacity:1, duration: 4.5});
tl.fromTo('.big-text', {opacity: 0}, {opacity:1, duration: 4.5}, '-=4.5');

