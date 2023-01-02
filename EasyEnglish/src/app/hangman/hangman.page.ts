import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-hangman',
  templateUrl: './hangman.page.html',
  styleUrls: ['./hangman.page.scss'],
})
export class HangmanPage implements OnInit {
  declare letterContainer: HTMLElement;
  declare optionsContainer: HTMLElement;
  declare userInputSection: HTMLElement;
  declare canvas: HTMLElement;
  declare options: any;

  constructor() {}

  chosenWord = '';

  ngOnInit() {
    this.letterContainer = document.getElementById('letter-container');
    this.optionsContainer = document.getElementById('options-container');
    this.userInputSection = document.getElementById('user-input-section');
    this.canvas = document.getElementById('canvas');

    this.options = {
      fruits: [
        'Apple',
        'Blueberry',
        'Mandarin',
        'Pineapple',
        'Pomegranate ',
        'Watermelon',
      ],
      animals: [
        'Hedgehog',
        'Rhinoceros',
        'Squirrel',
        'Panther ',
        'Walrus',
        'Zebra',
      ],
      countries: ['India', 'Hungary', 'Kyrgyzstan', 'Switzerland', 'Zimbabwe'],
    };

    displayOptions(this.optionsContainer, this.options);
  }
}
function displayOptions(optionsContainer: HTMLElement, options: any) {
  optionsContainer.innerHTML +=
    '<ion-card-header><ion-card-title color="dark">Please Select An Option</ion-card-title></ion-card-header>';
  let buttonCon = document.createElement('div');

  for (let value in options) {
    buttonCon.innerHTML += `<ion-button color="danger" class="options" (click)="generateWord(${value})" [disabled]="buttonDisabled">${value}</ion-button>`;
  }
  optionsContainer.appendChild(buttonCon);
}

function generateWord(optionValue: any) {
  let optionsButtons = document.querySelectorAll('.options');

  optionsButtons.forEach((button) => {

    let toast = this.toastCtrl.create({
      message: 'User was added successfully',
      duration: 3000,
      position: 'top'
    });

    toast.present();

    if (button.innerHTML.toLowerCase() === optionValue) {
      button.classList.add('active');
      
    }
    this.buttonDisabled = true;
  });
}
