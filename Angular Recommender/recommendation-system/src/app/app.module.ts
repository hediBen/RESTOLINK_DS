import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import {RouterModule, Routes} from '@angular/router';
import { DashbordComponent } from './dashbord/dashbord.component';

import { HttpClientModule } from '@angular/common/http';

import {AngularFireModule} from 'angularfire2';
import {AngularFirestoreModule} from 'angularfire2/firestore';
import {AngularFireAuthModule} from 'angularfire2/auth';
import {environment} from '../environments/environment';

import {AuthService} from './auth.service';
import { SignupComponent } from './signup/signup.component';
import { FormsModule} from '@angular/forms';
import { RecommendationsComponent } from './recommendations/recommendations.component';
import { NearbyRestComponent } from './nearby-rest/nearby-rest.component';


const appRoutes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'navbar', component: NavBarComponent},
  {path: 'dashbord', component: DashbordComponent},
  {path: 'signup', component: SignupComponent},
  {path: 'recommendations', component: RecommendationsComponent},
  {path: 'nearbyRes', component: NearbyRestComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavBarComponent,
    DashbordComponent,
    SignupComponent,
    RecommendationsComponent,
    NearbyRestComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
    AngularFireModule.initializeApp(environment.firebase),
    AngularFirestoreModule,
    AngularFireAuthModule,
    FormsModule


  ],
  providers: [AuthService, DashbordComponent , RecommendationsComponent , NearbyRestComponent ],
  bootstrap: [AppComponent]
})
export class AppModule { }
