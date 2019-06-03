<template>
  <form>
    <md-card>
      <md-card-header data-background-color="green">
        <h4 class="title">Produtos</h4>
        <p class="category">Criar produto</p>
      </md-card-header>

      <md-card-content>
        <form-create-product-base />
      </md-card-content>
    </md-card>

    <md-card>
      <md-card-header data-background-color="green">
        <h4 class="title">Produtos</h4>
        <p class="category">Adicionar fotos</p>
      </md-card-header>

      <md-card-content>
        <form-images-product />
      </md-card-content>
    </md-card>
  </form>
</template>
<script>
import FormCreateProductBase from "@/components/widgets/form/FormCreateProductBase.vue";
import FormImagesProduct from "@/components/widgets/form/FormImagesProduct.vue";

export default {
  name: "create-product-form",
  components: {
    FormCreateProductBase,
    FormImagesProduct
  }
};
</script>

<style></style>
