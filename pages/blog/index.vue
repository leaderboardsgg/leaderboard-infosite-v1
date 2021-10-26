<script>
export default {
  async asyncData({ $content }) {
    const posts = await $content().sortBy('date', 'desc', 'createdAt').fetch();

    return {
      posts,
    };
  },
};
</script>

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
      <h2 class="text-3xl text-center font-bold">New on the Blog</h2>

      <ul class="dark:text-gray-200 content-center grid grid-cols-3 gap-8 mt-8">
        <PostPreview
          v-for="post in posts"
          :key="post.slug"
          :post="post"
        ></PostPreview>
      </ul>
    </div>
  </div>
</template>
