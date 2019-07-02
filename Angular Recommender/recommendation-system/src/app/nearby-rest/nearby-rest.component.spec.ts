import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NearbyRestComponent } from './nearby-rest.component';

describe('NearbyRestComponent', () => {
  let component: NearbyRestComponent;
  let fixture: ComponentFixture<NearbyRestComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NearbyRestComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NearbyRestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
