<template>
  <div>
    <owl />
    <div class="form">
      <div class="control">
        <label for="login" class="fa fa-user" />
        <input id="text" placeholder="Login" type="text" />
      </div>
      <div class="control">
        <label for="password" class="fa fa-asterisk" />
        <input id="password" placeholder="Password" type="password" />
      </div>
    </div>
  </div>
</template>

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

<style scoped>
body {
  background-color: #3c3c3c;
  font-family: "Roboto", sans-serif;
  font-size: 14px;
}
.form {
  margin: auto;
  margin-top: -9px;
  padding: 30px;
  background-color: #fff;
  width: 300px;
  text-align: center;
}
.form .control {
  margin-bottom: 10px;
  position: relative;
}
.form .control label {
  position: absolute;
  font-size: 16px;
  top: 11px;
  left: 9px;
  color: rgba(0, 0, 0, 0.3);
}
.form .control input {
  padding: 9px 6px 9px 30px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 14px;
}
</style>
