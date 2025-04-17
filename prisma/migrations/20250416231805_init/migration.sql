-- CreateTable
CREATE TABLE "User" (
    "id" SERIAL NOT NULL,
    "produto" TEXT NOT NULL,
    "unidade" TEXT,
    "preco" TEXT NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_produto_key" ON "User"("produto");
