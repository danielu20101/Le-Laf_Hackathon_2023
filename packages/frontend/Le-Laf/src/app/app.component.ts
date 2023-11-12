import { Component } from '@angular/core';
import { ModalService } from './services/modal.service';
import { NavigationEnd, Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Le-Laf';
  showBar = false;
  current_url = "";
  
  constructor(public modalService: ModalService, public router:Router) { }
  
  ngOnInit(): void {

    this.current_url = this.router.url
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd ) {
        this.current_url = event.url;
        if(this.current_url == '/' || this.current_url == '/register') {
          this.showBar = false;
        }
        else
          this.showBar  = true;
      }
    });

    this.modalService.loggedInObservable().subscribe((data) => {
      this.showBar = data;
    })
  }

}
