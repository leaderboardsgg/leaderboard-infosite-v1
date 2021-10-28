<template>
  <div
    class="
      flex flex-grow
      justify-center
      p-5
      dark:bg-gray-800 dark:text-gray-300
    "
  >
    <div class="w-full rounded border border-gray-300 p-5">
      <h2 class="text-3xl text-center font-bold">Posts tagged "{{ tag }}"</h2>
      <h3 class="text-xl text-center font-medium">
        <nuxt-link to="/blog">← Back to all articles</nuxt-link>
      </h3>

      <ul class="dark:text-gray-300 content-center grid grid-cols-3 gap-8 mt-8">
        <PostPreview
          v-for="post in posts"
          :key="post.slug"
          :post="post"
        ></PostPreview>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  async asyncData({ $content, params }) {
    const tag = params.tag;
    const posts = await $content()
      .where({ tags: { $contains: tag } })
      .sortBy('date', 'desc', 'createdAt')
      .fetch();

    return {
      posts,
      tag,
    };
  },
};
</script>
