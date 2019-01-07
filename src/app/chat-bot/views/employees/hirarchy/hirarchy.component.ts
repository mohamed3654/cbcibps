import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-hirarchy',
  templateUrl: './hirarchy.component.html',
  styleUrls: ['./hirarchy.component.scss']
})
export class HirarchyComponent {

  public employees_date = [{
    level: 1,
    employees: [{
      id: 1,
      name: 'Ibrahim Mubark',
      avatar: 'https://pbs.twimg.com/profile_images/1078471113397555200/ro5vaMFW.jpg',
      role: 'Head of EPM',
      email: 'ibrahim.mubark@cibeg.com',
      cisco: '1234',
      expanded: false
    }]
  }, {
    level: 2,
    employees: [{
      id: 2,
      name: 'Peter Adel',
      avatar: 'https://pbs.twimg.com/profile_images/784059167401181188/tVh9xm9a.jpg',
      role: 'Consumer Banking, Digital Channels',
      email: 'Peter.adelnaguib@cibeg.com',
      cisco: '2206',
      expanded: false
    }, {
      id: 3,
      name: 'Karim Soliman',
      avatar: 'https://randomuser.me/api/portraits/men/86.jpg',
      role: 'Production',
      email: 'Karim.soliman@cibeg.com',
      cisco: '2229',
      expanded: false
    }, {
      id: 4,
      name: 'Mohamed AbdelFatah',
      avatar: 'https://pbs.twimg.com/profile_images/969073897189523456/rSuiu_Hr.jpg',
      role: 'Institutional Banking',
      email: 'mohamed.abdelfattah@cibeg.com',
      cisco: '2217',
      expanded: false
    }, {
      id: 5,
      name: 'Kamal Zaki',
      avatar: 'https://pbs.twimg.com/profile_images/946738414984065026/dJj9Z8uq.jpg',
      role: 'Risk & Support Functions',
      email: 'Kamal.zaki@cibeg.com',
      cisco: '2421',
      expanded: false
    }]
  }];

  toggleExpand(employee) {
    employee.expanded = !employee.expanded;
  }

}
