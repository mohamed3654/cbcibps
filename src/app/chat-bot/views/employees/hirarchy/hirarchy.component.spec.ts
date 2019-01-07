import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HirarchyComponent } from './hirarchy.component';

describe('HirarchyComponent', () => {
  let component: HirarchyComponent;
  let fixture: ComponentFixture<HirarchyComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HirarchyComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HirarchyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
