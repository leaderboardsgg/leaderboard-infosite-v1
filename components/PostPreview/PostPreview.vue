<template>
  <li
    class="
      dark:bg-gray-900
      bg-gray-200
      rounded-lg
      p-1
      pb-3
      transition-all
      duration-500
      ease-in-out
    "
  >
    <a :href="`/posts/${post.slug}`">
      <h2 class="mt-2 text-2xl font-bold px-1">{{ post.title }}</h2>
      <span class="mt-2 text-xs font-semibold px-1">{{
        formatDate(post.date)
      }}</span>
      <span v-if="post.tags" class="space-x-1 mt-2">
        <span
          v-for="tag in post.tags"
          :key="tag"
          class="rounded-lg px-1.5 text-gray-100 text-sm font-bold"
          :class="'tag-' + tag.toLowerCase()"
        >
          <nuxt-link :to="`/blog/tag/${tag}`">{{ tag }}</nuxt-link>
        </span>
      </span>
      <p class="mt-2 px-1">
        {{ post.description }}
      </p>
    </a>
  </li>
</template>

<script lang="ts">
export default {
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  methods: {
    formatDate(date: string): string {
      const format = new Intl.DateTimeFormat('en', {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
      });
      return format.format(new Date(date));
    },
  },
};
</script>
