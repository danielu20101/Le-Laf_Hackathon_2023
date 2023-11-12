import { Component } from '@angular/core';
import { ModalService } from './services/modal.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Le-Laf';
  showBar = false;

  constructor(public modalService: ModalService, public router:Router) { }


  ngOnInit(): void {

    this.modalService.loggedInObservable().subscribe((data) => {
      this.showBar = data;
    })
    let current_url = this.router.url
    if(current_url == '/' || current_url == '/register') {
      this.showBar = false;
    }
    else
      this.showBar  = true;
  }

}
