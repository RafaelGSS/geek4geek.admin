<template>
  <div class="owl">
    <div class="hand"></div>
    <div class="hand hand-r"></div>
    <div class="arms">
      <div class="arm"></div>
      <div class="arm arm-r"></div>
    </div>
  </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.owl {
  margin: auto;
  width: 211px;
  height: 108px;
  background-image: url("https://dash.readme.io/img/owl-login.png");
  position: relative;
}
.owl .hand {
  width: 34px;
  height: 34px;
  border-radius: 40px;
  background-color: #472d20;
  transform: scaleY(0.6);
  position: absolute;
  left: 14px;
  bottom: -8px;
  transition: 0.3s ease-out;
}
.owl .hand.password {
  transform: translateX(42px) translateY(-15px) scale(0.7);
}
.owl .hand.hand-r {
  left: 170px;
}
.owl .hand.hand-r.password {
  transform: translateX(-42px) translateY(-15px) scale(0.7);
}
.owl .arms {
  position: absolute;
  top: 58px;
  height: 41px;
  width: 100%;
  overflow: hidden;
}
.owl .arms .arm {
  width: 40px;
  height: 65px;
  background-image: url("https://dash.readme.io/img/owl-login-arm.png");
  position: absolute;
  left: 20px;
  top: 40px;
  transition: 0.3s ease-out;
}
.owl .arms .arm.password {
  transform: translateX(40px) translateY(-40px);
}
.owl .arms .arm.arm-r {
  left: 158px;
  transform: scaleX(-1);
}
.owl .arms .arm.arm-r.password {
  transform: translateX(-40px) translateY(-40px) scaleX(-1);
}
</style>

