let state = {
    skin: 0,
    dress: 0,
    top: 0,
    bottom: 0,
    hair: 0,
    accessory: 0,
    shoes: 0,
    face: 0,
    isDressVisible: true,  // Track whether dress or top/bottom is visible
};

function updateClass(elementId, classNamePrefix, stateValue, maxState) {
    let element = document.querySelector(`#${elementId}`);
    if (stateValue < maxState) {
        stateValue++;
    } else {
        stateValue = 0;
    }
    element.setAttribute("class", `${classNamePrefix}${stateValue}`);
    return stateValue;
}

function nextSkin() {
    state.skin = updateClass("skin", "skin", state.skin, 3);
}

function nextDress() {
    state.isDressVisible = true;
    document.querySelector("#dress").style.display = "block";
    document.querySelector("#top").style.display = "none";
    document.querySelector("#bottom").style.display = "none";
    state.dress = updateClass("dress", "dress", state.dress, 7);
}

function nextTop() {
    state.isDressVisible = false;
    document.querySelector("#dress").style.display = "none";
    document.querySelector("#top").style.display = "block";
    document.querySelector("#bottom").style.display = "block";
    state.top = updateClass("top", "top", state.top, 7);
}

function nextBottom() {
    state.isDressVisible = false;
    document.querySelector("#dress").style.display = "none";
    document.querySelector("#top").style.display = "block";
    document.querySelector("#bottom").style.display = "block";
    state.bottom = updateClass("bottom", "bottom", state.bottom, 6);
}

function nextHair() {
    state.hair = updateClass("hair", "hair", state.hair, 5);
}

function nextAccessory() {
    state.accessory = updateClass("accessory", "access", state.accessory, 3);
}

function nextShoes() {
    state.shoes = updateClass("shoes", "shoes", state.shoes, 3);
}

function nextFace() {
    state.face = updateClass("face", "face", state.face, 2);
}

document.getElementById("nextskin").addEventListener("click", nextSkin);
document.getElementById("nextface").addEventListener("click", nextFace);
document.getElementById("nexthair").addEventListener("click", nextHair);
document.getElementById("nextdress").addEventListener("click", nextDress);
document.getElementById("nexttop").addEventListener("click", nextTop);
document.getElementById("nextbottom").addEventListener("click", nextBottom);
document.getElementById("nextshoes").addEventListener("click", nextShoes);
document.getElementById("nextaccessory").addEventListener("click", nextAccessory);

// Initialize the avatar components
nextSkin();
nextFace();
nextHair();
nextDress();
nextShoes();
nextAccessory();
