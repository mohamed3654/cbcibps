import { LOGO_PATH } from './../../../shared/utilities/defines';
import { Component } from '@angular/core';

@Component({
  selector: 'app-main-header',
  templateUrl: './main-header.component.html',
  styleUrls: ['./main-header.component.scss']
})
export class MainHeaderComponent {
  /**
   * @property logoPath
   * @type {string}
   */
  public logoPath = LOGO_PATH;
}
