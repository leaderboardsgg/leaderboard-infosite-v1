<template>
  <div class="dark:bg-gray-800 dark:text-gray-300 border-b border-gray-300">
    <div
      class="
        container
        relative
        flex flex-wrap
        lg:flex-row
        justify-between
        mr-auto
        px-3
        py-3
      "
    >
      <div class="flex flex-grow">
        <NuxtLink class="flex ml-4" to="/">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-10 w-10 mx-1"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <h1
            v-show="lg"
            class="
              w-full
              py-2
              text-lg text-center
              md:text-left
              font-semibold
              leading-6
              tracking-tight
              hidden
              md:inline
            "
          >
            Leaderboards.gg
          </h1>
        </NuxtLink>
      </div>
      <div
        class="
          border-t border-gray-300
          lg:border-t-0
          flex flex-col
          lg:flex-row
          mt-2
          lg:mt-0
          w-full
          lg:w-auto
          space-y-2
          lg:space-y-0
        "
      >
        <CoreNavLinks />
      </div>
      <div
        class="
          flex flex-row
          items-center
          absolute
          right-2
          top-4
          lg:relative lg:right-0 lg:top-0
          space-x-2
          lg:space-x-0
        "
      >
        <select
          v-model="$colorMode.preference"
          class="h-8 px-1 dark:bg-gray-900 dark:border-gray-700"
        >
          <option value="system">System</option>
          <option value="dark">Dark</option>
          <option value="light">Light</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from '@nuxtjs/composition-api';
import { useBreakpoints } from '@vueuse/core';
import { theme } from '../../tailwind.config';
const breakpoints = useBreakpoints(theme.screens);

export default defineComponent({
  setup() {
    const lg = breakpoints.greater('lg');
    const mobileNavIsActive = ref(false);

    return {
      lg,
      mobileNavIsActive,
    };
  },
});
</script>
