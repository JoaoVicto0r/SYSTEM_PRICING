import { Module } from '@nestjs/common';
import { PrismaModule } from './prisma/prisma.module';
import { UserService } from './user/user.service';
import { UserController } from './user/user.controller';

@Module({
  imports: [PrismaModule],
  controllers: [UserController],
  providers: [UserService],
})
export class AppModule {}
