<template>
  <md-card class="md-card-profile">
    <div class="md-card-avatar">
      <img class="img" :src="cardUserImage" />
    </div>

    <md-card-content>
      <h6 class="category text-gray">CEO / e Fundador</h6>
      <h4 class="card-title">Primo do Steve Jobs</h4>
      <p class="card-description">
        Um cara que não estudava na faculdade e por sorte viu que a vida,
        não era assim e começõu a estudar pra ter um futuro e hoje ele trabalha
        de programador em uma empresa imobiliária e sócio de um Ecommerce...
      </p>
      <a href="https://github.com/yuresilva" target="_blank"> <md-button class="md-round md-success">Seguir ele no Github</md-button> </a>
    </md-card-content>
  </md-card>
</template>
<script>
export default {
  name: "user-card",
  props: {
    cardUserImage: {
      type: String,
      default: require("@/assets/img/faces/img-adm.jpg")
    }
  },
  data() {
    return {};
  }
};
</script>
<style></style>
