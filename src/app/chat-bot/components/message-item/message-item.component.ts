import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-message-item',
  templateUrl: './message-item.component.html',
  styleUrls: ['./message-item.component.scss']
})
export class MessageItemComponent {
  /** Message Item */
  @Input() message: string;
  /** is message By current user */
  @Input() byMe = false;
}
