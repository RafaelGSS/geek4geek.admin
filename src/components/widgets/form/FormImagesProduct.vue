<template>
  <div class="md-layout">
    <div class="md-layout-item md-small-size-100 md-size-33">
      <md-field>
        <label>Imagem Normal</label>
        <md-input name="display_image" type="text" required></md-input>
      </md-field>
    </div>
    <div class="md-layout-item md-small-size-100 md-size-33">
      <md-field>
        <label>Imagem Baixa Resolução</label>
        <md-input name="low_display_image" type="text"></md-input>
      </md-field>
    </div>
    <div class="md-layout-item md-small-size-100 md-size-33">
      <md-field>
        <label>Imagem Alta Resolução</label>
        <md-input name="big_display_image" type="text"></md-input>
      </md-field>
    </div>
    <div class="md-layout-item md-size-100 text-right" v-if="submit">
      <md-button @click="$emit('submit')" class="md-raised md-success"
        >Criar Imagem</md-button
      >
    </div>
  </div>
</template>

<script>
export default {
  props: {
    submit: {
      type: Boolean,
      default: false
    }
  }
};
</script>
