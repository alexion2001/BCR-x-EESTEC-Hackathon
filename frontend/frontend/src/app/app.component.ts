import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DateExtrasService } from './date-extras.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'frontend';
  constructor(
    private router: Router,
    private dateExtrasService: DateExtrasService
    ) {
    
  }
  food = 0;
  home = 0;
  transport = 0;
  total = 0;
  foodAngle = 0;
  homeAngle = 0;
  transportAngle = 0;
  rataMax=0;
  titular = "Dinu"
  foodPercent = 0;
  homePercent = 0;
  transportPercent = 0;
  ngOnInit(): void {

    this.dateExtrasService.getData().subscribe(
      (result) => {
          console.log(result);
          this.food = Math.round(result['mancare']);
          this.home = Math.round(result['casa']);
          this.transport = Math.round(result['transport']);
          this.titular = result['titular'];
          this.total = Math.round(result['venit']);

          this.foodPercent =   Math.round(result['mancareProc']*100);
          this.homePercent = Math.round(result['casaProc']*100);
          this.transportPercent = Math.round(result['transportProc']*100);

          this.foodAngle = 360 * result['mancareProc'];
          
          this.homeAngle = this.foodAngle + 360 * result['casaProc'];
          this.transportAngle = this.homeAngle + 360 * result['transportProc'];
          // this.rataMax=this.total*0.75-this.food-this.transport-this.home;
          this.rataMax=this.total*0.8-this.food-this.transport-this.home;
          if(this.rataMax < 0) this.rataMax = 0;
          console.log(this.foodAngle);
          document.getElementById("piechart")!.style.backgroundImage = "conic-gradient(#739df3 "+ `${this.foodAngle}deg` + ", #695dcb 0 " + `${this.homeAngle}deg` +",#a96ce3 0 " + `${this.transportAngle}deg` + ",#2e5f99 0)"; 
          
      },
      (error) => {
        console.error(error);
      }
      
    );


    
  
  
  
  }
}
  