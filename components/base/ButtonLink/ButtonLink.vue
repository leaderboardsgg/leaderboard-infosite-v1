<template>
  <NuxtLink class="button-link dark" v-bind="$attrs" v-on="$listeners">
    <slot> Placeholder </slot>
  </NuxtLink>
</template>

<style>
.button-link {
  @apply rounded px-4 py-3 text-current hover:bg-current;
}
</style>
