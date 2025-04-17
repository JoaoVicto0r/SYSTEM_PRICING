import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import * as dotenv from 'dotenv';
import { User } from './user/user.entity';
import { UserService } from './user/user.service';
import { UserController } from './user/user.controller';
import { UserModule } from './user/user.module';
import { PrismaService } from './prisma/prisma.service';


dotenv.config();

const isOffline = process.env.DB_TYPE === 'sqlite';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: isOffline ? 'sqlite' : 'postgres',
      database: isOffline ? process.env.SQLITE_DATABASE : process.env.POSTGRES_DB,
      host: isOffline ? undefined : process.env.POSTGRES_HOST,
      port: isOffline ? undefined : Number(process.env.POSTGRES_PORT),
      username: isOffline ? undefined : process.env.POSTGRES_USER,
      password: isOffline ? undefined : process.env.POSTGRES_PASSWORD,
      entities: [User],
      synchronize: true,
    }),
    UserModule
  ],
  providers: [PrismaService],





  
})
export class AppModule {}

