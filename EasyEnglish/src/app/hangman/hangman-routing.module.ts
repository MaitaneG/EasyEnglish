import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HangmanPage } from './hangman.page';

const routes: Routes = [
  {
    path: '',
    component: HangmanPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class HangmanPageRoutingModule {}
