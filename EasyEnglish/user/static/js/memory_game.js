const card = document.querySelectorAll('.cell');
const front = document.querySelectorAll('.front');
var attempts = 0;

const clicking = () => {
    for (let i = 0; i < card.length; i++) {
    card[i].addEventListener('click', (e) => {
        
        front[i].classList.add('flip');
        const flipped = document.querySelectorAll('.flip');

        if (flipped.length == 2) {
            match(flipped[0], flipped[1]);
        }
    });
    }
}

const match = (flipped1, flipped2) => {
    if (flipped1.dataset['index'] == flipped2.dataset['index']) {
        cardsAreTheSame(flipped1, flipped2);
    } else {
        cardsNotTheSame(flipped1, flipped2);
    }
}

const cardsAreTheSame=(card1, card2)=>{
    card1.classList.remove('flip');
    card2.classList.remove('flip');

    card1.classList.add('matched');
    card2.classList.add('matched');

    const matched = document.querySelectorAll('.matched');
    if(matched.length==16){
        alert("Bukatu duzu");
    }
}

const cardsNotTheSame=(card1, card2)=>{
    attempts++;

    if (attempts < 5) {
        setTimeout(() => {
            card1.classList.remove('flip');
            card2.classList.remove('flip');
        }, 1000);
    } else {
        this.alert('Saiakera guztiak agortu dituzu');
    }
}

window.onload = clicking;