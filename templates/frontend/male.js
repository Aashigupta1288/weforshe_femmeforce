let state = {
    skin: 0,
    top: 0,
    bottom: 0,
    hair: 0,
    accessory: 0,
    shoes: 0,
    face: 0,
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
    state.skin = updateClass("skin", "skin", state.skin, 3); // Adjust based on the number of skin options
}

function nextTop() {
    state.top = updateClass("top", "top", state.top, 11); // Adjust based on the number of top options
}

function nextBottom() {
    state.bottom = updateClass("bottom", "bottom", state.bottom, 9); // Adjust based on the number of bottom options
}

function nextHair() {
    state.hair = updateClass("hair", "hair", state.hair, 4); // Adjust based on the number of hair options
}

function nextAccessory() {
    state.accessory = updateClass("accessory", "access", state.accessory, 3); // Adjust based on the number of accessory options
}

function nextShoes() {
    state.shoes = updateClass("shoes", "shoes", state.shoes, 2); // Adjust based on the number of shoes options
}

function nextFace() {
    state.face = updateClass("face", "face", state.face, 3); // Adjust based on the number of face options
}

document.getElementById("nextskin").addEventListener("click", nextSkin);
document.getElementById("nextface").addEventListener("click", nextFace);
document.getElementById("nexthair").addEventListener("click", nextHair);
document.getElementById("nexttop").addEventListener("click", nextTop);
document.getElementById("nextbottom").addEventListener("click", nextBottom);
document.getElementById("nextshoes").addEventListener("click", nextShoes);
document.getElementById("nextaccessory").addEventListener("click", nextAccessory);

// Initialize the avatar components
nextSkin();
nextFace();
nextHair();
nextTop();
nextBottom();
nextShoes();
nextAccessory();
