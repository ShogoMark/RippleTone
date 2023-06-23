const burger = document.querySelector('.burger');
const overLay = document.querySelector('.overlay');
const close = document.querySelector('.close')
const hidden = document.querySelector('.hidden')
const body = document.querySelector('body');
const nav = document.querySelector('.navbar');
const simple = document.querySelector('.simple')
const speedy = document.querySelector('.speedy')
const easy = document.querySelector('.easy')
const bookmark = document.querySelector('.bookmark')
const intelligent = document.querySelector('.intelligent')
const share = document.querySelector('.share')


speedy.addEventListener('click', () => {
    if (intelligent.classList.contains("has_fade")){
        intelligent.classList.remove('has_fade')
        bookmark.classList.add('has_fade')
        share.classList.add('has_fade')

    }
})

simple.addEventListener('click', () => {
    if (bookmark.classList.contains("has_fade")){
        bookmark.classList.remove('has_fade')
        intelligent.classList.add('has_fade')
        share.classList.add('has_fade')

    }
})

easy.addEventListener('click', () => {
    if (share.classList.contains("has_fade")){
        share.classList.remove('has_fade')
        intelligent.classList.add('has_fade')
        bookmark.classList.add('has_fade')

    }
})


burger.addEventListener('click', () => {

if(nav.classList.contains('navbar')){
    overLay.classList.remove('hidden');
    body.classList.add('noscroll');
    overLay.classList.add('fade-in');
    overLay.classList.remove('fade-out');
    }
})


close.addEventListener('click', () => {
    if(nav.classList.contains('navbar')){
        overLay.classList.add('hidden');
        overLay.classList.add('fade-out');
        overLay.classList.remove('fade-in');
        body.classList.remove('noscroll');  
    }
});

const quest = document.querySelectorAll('.question')

quest.forEach(function (question) {
    const btn = question.querySelector('.question_btn');
    const ans = question.querySelector('.answer')
    const arrow = question.querySelector('.arrow_svg')
    const color = question.querySelector('.color');
  
    btn.addEventListener('click', function(){
        quest.forEach(element => {
            //console.log(element);
              // console.log(element !== question);
              if(element !== question){
                arrow.classList.toggle('rotate')
                color.classList.toggle('stroke')
                ans.classList.toggle('has_fade')
              }
        });
     
    })



});