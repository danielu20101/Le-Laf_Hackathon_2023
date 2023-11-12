import { Component } from '@angular/core';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-request',
  templateUrl: './request.component.html',
  styleUrls: ['./request.component.css'],
})
export class RequestComponent {
  viewDate = new Date();
  events = [];
  refresh = new Subject<void>();
  activeDayIsOpen = false;
}
