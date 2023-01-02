import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { HangmanPageRoutingModule } from './hangman-routing.module';

import { HangmanPage } from './hangman.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    HangmanPageRoutingModule
  ],
  declarations: [HangmanPage]
})
export class HangmanPageModule {}
