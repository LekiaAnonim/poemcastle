
let allDiv = document.querySelectorAll('div');


function displayDropDown() {
    document.querySelector('.list-of-collections').classList.toggle('display');
    document.querySelector('.drop-down-icon svg').classList.toggle('rotate180');
}

const swiper = new Swiper(".swiper", {
    slidesPerView: 4,
    spaceBetween: 50,
    loop: true,
    grabCursor: true,
    centeredSlides: true,
    slideActiveClass: "active",
    navigation: {
      nextEl: ".next",
      prevEl: ".prev"
    },
    pagination: {
      el: ".pagination",
      clickable: true
    },
    autoplay: {
      enabled: true,
      delay: 5000
    },
    // Media
    // breakpoints: {
    //   // when window width is >= 320px
    //   320: {
    //     slidesPerView: 2,
    //     spaceBetween: 20
    //   },
    //   // when window width is >= 480px
    //   480: {
    //     slidesPerView: 4,
    //     spaceBetween: 30
    //   },
    // }
  });

let collectionHamList = document.querySelector('.collections-list');
function displayCollectionList() {
  document.querySelector('.collections-list').classList.toggle('display-collection-list');
}

function removeHamCard() {
    document.querySelector('.hamburger-menu-card').classList.add('remove-ham-menu-card');
}
function displayHamCard() {
    document.querySelector('.hamburger-menu-card').classList.remove('remove-ham-menu-card');
}