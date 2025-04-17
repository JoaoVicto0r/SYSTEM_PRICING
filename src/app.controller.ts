import { Controller, Get, UnsupportedMediaTypeException } from '@nestjs/common';
import { AppService } from './app.service';
import { resolveSoa } from 'dns';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  
}
