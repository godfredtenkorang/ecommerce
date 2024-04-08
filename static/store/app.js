var message_timeout = document.getElementById("message-timer");

setTimeout(function () {
    
    message_timeout.style.display = "none";

}, 2500);


$(".bars").click(() => {
    $(".mobile__nav__fade__and__show__circle").toggleClass("open");
    $(".mobile__nav__fade__and__show").toggleClass("open");
    $(".bars").toggleClass("toggle")
    
})

const allStar = document.querySelectorAll('.rating .star')
        const ratingValue = document.querySelector('.rating input')

        allStar.forEach((item, idx) => {
            item.addEventListener('click', function () {
                let click = 0
                ratingValue.value = idx + 1

                allStar.forEach(i => {
                    i.classList.replace('bxs-star', 'bx-star')
                    i.classList.remove('active')
                })
                for (let i = 0; i < allStar.length; i++) {
                    if (i <= idx) {
                        allStar[i].classList.replace('bx-star', 'bxs-star')
                        allStar[i].classList.add('active')
                    } else {
                        allStar[i].style.setProperty('--i', click)
                        click++
                    }
                }
            })
        })

