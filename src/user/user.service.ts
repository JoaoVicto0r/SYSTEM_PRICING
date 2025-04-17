import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { CreateUserDto } from './dto/create-user.dto';

@Injectable()
export class UserService {
  constructor(private readonly prisma: PrismaService) {}

  async create(data: CreateUserDto) {
    return this.prisma.user.create({
      data: {
        ...data,
        preco: data.preco, 
      },
    });
  }

  
  async findAll() {
    return this.prisma.user.findMany();
  }
}
