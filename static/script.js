let prevScrollPos = window.pageYOffset;

window.onscroll = function() {
    const currentScrollPos = window.pageYOffset;

    if (prevScrollPos > currentScrollPos) {
        document.getElementById("bottomBar").classList.remove("show");
        

    } else {
        document.getElementById("bottomBar").classList.add("show");
    }

    prevScrollPos = currentScrollPos;
};