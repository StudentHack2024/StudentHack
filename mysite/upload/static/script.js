// The following uses some code from the following repository:
// https://github.com/gjmolter/web-3dmodel-threejs

import * as THREE from "https://cdn.skypack.dev/three@0.129.0/build/three.module.js";
import { OrbitControls } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/controls/OrbitControls.js";
import { GLTFLoader } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/GLTFLoader.js";


//Create a Three.JS Scene
const scene = new THREE.Scene();

//create a new camera with positions and angles
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

//Keep track of the mouse position
let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;

let object;
let controls;

//Set which object to render
let objToRender = 'galaxy';

//Instantiate a loader for the .gltf file
const loader = new GLTFLoader();

//Load the file
loader.load(
  `static/assets/models/${objToRender}/scene.gltf`,
  function (gltf) {
    //If the file is loaded, add it to the scene
    object = gltf.scene;
    scene.add(object);

    object.scale.set(150, 150, 150);
  },
  function (xhr) {
    //While it is loading, log the progress
    console.log((xhr.loaded / xhr.total * 100) + '% loaded');
  },
  function (error) {
    //If there is an error, log it
    console.error(error);
  }
);

//Instantiate a new renderer and set its size
const renderer = new THREE.WebGLRenderer({ alpha: false });
renderer.setSize(window.innerWidth, window.innerHeight);

//Add the renderer to the DOM
document.getElementById("container3D").appendChild(renderer.domElement);

//Set how far the camera will be from the 3D model
camera.position.z = 300;
camera.position.y = 200;

//Add lights to the scene
const topLight = new THREE.DirectionalLight(0xffffff, 1);
topLight.position.set(500, 500, 500)
topLight.castShadow = true;
scene.add(topLight);

const ambientLight = new THREE.AmbientLight(0x333333, 10);
scene.add(ambientLight);

//This adds controls to the camera
controls = new OrbitControls(camera, renderer.domElement);
controls.enableZoom = false; //Disable zoom

//Render the scene
function animate() {
  requestAnimationFrame(animate);

  renderer.render(scene, camera);
}

//Add a listener to the window, so we can resize the window and the camera
window.addEventListener("resize", function () {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// Add an event listener for the scroll event
window.addEventListener('wheel', function(event) {
    // Check if the object is loaded
    if (object) {
      // Update the rotation of the object based on the scroll delta
      object.rotation.y += event.deltaY * 0.001; // You can adjust the multiplier to get the desired speed
    }

    // Update the scale of the object based on the scroll delta
    let scaleChange = event.deltaY * 0.1; // You can adjust the multiplier to get the desired speed

    if (object.scale.x - scaleChange < 0 && object.scale.y - scaleChange < 0 && object.scale.z - scaleChange < 0){
        object.scale.set(0,0,0);
        var element = document.getElementById("form-total");
        console.log("opacity")
        console.log(element.style.opacity)
        if ((parseFloat(element.style.opacity) + 0.01) < 1.0){
            element.style.opacity = parseFloat(element.style.opacity) + 0.01;
        }
        var currentTranslateY = parseFloat(element.style.transform.replace('translateY(', '').replace('px)', ''));
        if (currentTranslateY - 5 >= 0){
            element.style.transform = "translateY(" + (currentTranslateY - 5) + "px)"
        }
    } else if (object.scale.x - scaleChange > 150 && object.scale.y - scaleChange > 150 && object.scale.z - scaleChange > 150){
        object.scale.set(150,150,150);
    } else if (object.scale.x >= 0 && object.scale.y >= 0 && object.scale.z >= 0){
        object.scale.set(
            object.scale.x - scaleChange,
            object.scale.y - scaleChange,
            object.scale.z - scaleChange
        );
    }
  });

//add mouse position listener, so we can make the eye move
document.onmousemove = (e) => {
  mouseX = e.clientX;
  mouseY = e.clientY;
}

//Start the 3D rendering
animate();