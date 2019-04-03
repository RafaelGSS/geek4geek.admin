<template>
  <div class="container">
   
    <div class="content">
       <owl/>
      <md-card>
        <md-card-header :data-background-color="dataBackgroundColor">
          <h4 class="title text-center">Bem Vindo</h4>
        </md-card-header>
        <md-card-content>
          <div class="content">
            <div class="md-layout">
              <div class="md-layout-item md-small-size-100 md-size-100">
                <md-field>
                  <label>User Name</label>
                  <md-input v-model="username" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-small-size-100 md-size-100">
                <md-field>
                  <label>Password</label>
                  <md-input v-model="address" type="password"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-size-100 text-center">
                <md-button class="md-raised md-success">Entrar</md-button>
              </div>
            </div>
          </div>
        </md-card-content>
      </md-card>
      </div>
  </div>
</template>

<style scoped>

body {
  background-color: #3c3c3c;
  font-family: "Roboto", sans-serif;
  font-size: 14px;
  margin: 0px
}

.container {
  width: 100vw;
  height: 100vh;
  background: #6C7A89;
  flex-direction: row;
  justify-content: center;
  align-items: center
}

b.md-card .md-card-header,
.md-card .md-card-header{
    margin-top: -30px;
    background: #282829;
}
.content{
  max-width: 500px;
  margin: auto;
}
@media screen and (max-width: 600px) {
.content{
  width: 100%;
  }
}
.title {
  font-weight: 900;
  font-size: 40px;
}
</style>

<script>
import JQuery from "jquery";
import Owl from "@/components/Animate/Owl";

let $ = JQuery;

export default {
  components: {
    Owl
  },
  mounted() {
    $('input[type="password"]')
      .on("focus", () => {
        $("*").addClass("password");
      })
      .on("focusout", () => {
        $("*").removeClass("password");
      });
  }
};
</script>

