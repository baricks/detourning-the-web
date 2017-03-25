window.onload = function() {
  Player.init();
}

Player = {
  init: function() {
    Player.container = document.getElementById("webgl-player");

    Player.size = {
      width: Player.container.offsetWidth,
      height: Player.container.offsetHeight
    };

    Player.scene = new THREE.Scene();
    Player.camera = new THREE.PerspectiveCamera(5, Player.size.width / Player.size.height, 2, 8000);
    Player.camera.position.z = 100;
    Player.scene.add(Player.camera);

    Player.light = new THREE.AmbientLight();
    Player.scene.add(Player.light);

    textureLoader1 = new THREE.TextureLoader();

    textureLoader1.load("./object/10.isomap.png", function(texture) {
      Player.texture1 = texture;
      Player.loadModel();
    });

    textureLoader2 = new THREE.TextureLoader();

    textureLoader2.load("./object/11.isomap.png", function(texture) {
      Player.texture2 = texture;
      Player.loadModel();
    });

    textureLoader3 = new THREE.TextureLoader();

    textureLoader3.load("./object/12.isomap.png", function(texture) {
      Player.texture3 = texture;
      Player.loadModel();
    });

    Player.renderer = new THREE.WebGLRenderer( { alpha: true } );

    Player.renderer.setSize(Player.size.width, Player.size.height);
    Player.container.appendChild(Player.renderer.domElement);

    Player.controls1 = new THREE.TrackballControls(Player.camera, Player.container);
    Player.controls2 = new THREE.TrackballControls(Player.camera, Player.container);

    Player.animate();
  },

  loadModel: function() {
    objectLoader1 = new THREE.OBJLoader();

    objectLoader1.load("./object/10.obj", function(object) {
      object.traverse(function(child) {
        if (child instanceof THREE.Mesh) {
          child.material.map = Player.texture1;
        }
      });
      object.position.x = - 200;
      Player.scene.add(object);
    });

    objectLoader2 = new THREE.OBJLoader();

    objectLoader2.load("./object/11.obj", function(object) {
      object.traverse(function(child) {
        if (child instanceof THREE.Mesh) {
          child.material.map = Player.texture2;
        }
      });
      object.position.x = 0;
      Player.scene.add(object);
    });

    objectLoader3 = new THREE.OBJLoader();

    objectLoader3.load("./object/12.obj", function(object) {
      object.traverse(function(child) {
        if (child instanceof THREE.Mesh) {
          child.material.map = Player.texture3;
        }
      });
      object.position.x = 200;
      Player.scene.add(object);
    });
  },

  animate: function() {
    requestAnimationFrame(Player.animate);
    Player.controls1.update();
    Player.controls2.update();
    Player.renderer.render(Player.scene, Player.camera);
  }
};
