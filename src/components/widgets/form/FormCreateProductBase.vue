<template>
  <div class="md-layout">
    <div class="md-layout-item md-small-size-100 md-size-33">
      <md-field>
        <label>Vendedor</label>
        <md-select name="id_seller" required>
          <md-option value="geek4geek">Geek4Geek</md-option>
        </md-select>
      </md-field>
    </div>
    <div class="md-layout-item md-small-size-100 md-size-33">
      <md-field>
        <label>Marca</label>
        <md-select name="id_brand" required>
          <md-option value="geek4geek">Geek4Geek</md-option>
        </md-select>
      </md-field>
    </div>
    <div class="md-layout-item md-small-size-100 md-size-33">
      <md-field>
        <label>Nome</label>
        <md-input name="name" type="text" required></md-input>
      </md-field>
    </div>
    <div class="md-layout-item md-small-size-100 md-size-50">
      <md-field>
        <label>Nome único</label>
        <md-input name="unique_name" type="text" required></md-input>
      </md-field>
    </div>
    <div class="md-layout-item md-small-size-100 md-size-50">
      <md-field>
        <label>Estoque</label>
        <md-input name="stock" type="number" required></md-input>
      </md-field>
    </div>
    <div class="md-layout-item md-small-size-100 md-size-100">
      <md-field>
        <label>Descrição curta</label>
        <md-input name="display_description" type="text" required></md-input>
      </md-field>
    </div>
    <div class="md-layout-item md-small-size-100 md-size-33">
      <md-field>
        <label>Preço</label>
        <md-input name="price" type="text" required></md-input>
      </md-field>
    </div>
    <div class="md-layout-item md-small-size-100 md-size-33">
      <md-field>
        <label>SKU</label>
        <md-input name="seller_custom_field" type="text"></md-input>
      </md-field>
    </div>
    <div class="md-layout-item md-size-100">
      <md-field maxlength="5">
        <label>Descrição completa</label>
        <md-textarea name="full_decription"></md-textarea>
      </md-field>
    </div>
    <div class="md-layout-item md-size-100 text-right">
      <md-button class="md-raised md-success">Criar produto</md-button>
    </div>
  </div>
</template>
