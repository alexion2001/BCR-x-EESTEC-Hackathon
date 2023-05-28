import { TestBed } from '@angular/core/testing';

import { DateExtrasService } from './date-extras.service';

describe('DateExtrasService', () => {
  let service: DateExtrasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DateExtrasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
