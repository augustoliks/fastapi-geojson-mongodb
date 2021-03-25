# py-ze-delivery 

API REST que simula o funcionamento de Backend do aplicativo Zé Delivery. O projeto foi criado para exercitar os seguintes pontos:

- **Performance:** Desempenho na consulta de dados;
- **Testabilidade:** Facilidade em testar e adicionar novos testes;
- **Manutenibilidade:** Facilidade adicionar novas funcionalidades;
- **Separação de conceitos:** (https://en.wikipedia.org/wiki/Separation_of_concerns)

## 1. Funcionalidades/Requisitos

### 1.1. Criar um parceiro:

Salvar no banco de dados **todas** as seguintes informações representadas por este JSON junto com as regras subsequentes:

```json
{
  "id": 1, 
  "tradingName": "Adega da Cerveja - Pinheiros",
  "ownerName": "Zé da Silva",
  "document": "1432132123891/0001",
  "coverageArea": { 
    "type": "MultiPolygon", 
    "coordinates": [
      [[[30, 20], [45, 40], [10, 40], [30, 20]]], 
      [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
    ]
  },
  "address": { 
    "type": "Point",
    "coordinates": [-46.57421, -21.785741]
  }
}
```

1. O campo `address` (endereço em inglês) segue o formato `GeoJSON Point` (https://en.wikipedia.org/wiki/GeoJSON);
2. o campo `coverageArea` (área de cobertura em inglês) segue o formato `GeoJSON MultiPolygon` (https://en.wikipedia.org/wiki/GeoJSON);
3. O campo `document` deve ser único entre os parceiros;
4. O campo `id` deve ser único entre os parceiros, mas não necessariamente um número inteiro;

### 1.2. Carregar parceiro pelo `id`:

Retornar um parceiro específico baseado no seu campo `id` com todos os campos apresentados acima.

### 1.3. Buscar parceiro:

Dada uma localização pelo usuário da API (coordenadas `long` e `lat`), procure o parceiro que esteja **mais próximo** e **que cuja área de cobertura inclua** a localização.
