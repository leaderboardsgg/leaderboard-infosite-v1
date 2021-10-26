<script>
export default {
  async asyncData({ $content, params }) {
    const post = await $content(params.slug).fetch();
    return { post };
  },
  head() {
    return {
      meta: [
        // Open Graph
        { content: this.post.title, hid: 'og:title', property: 'og:title' },
        { content: 'article', hid: 'og:type', property: 'og:type' },
        // Twitter Card
        {
          content: this.post.title,
          hid: 'twitter:title',
          name: 'twitter:title',
        },
      ],
      title: this.post.title,
    };
  },
  methods: {
    formatDate(date) {
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

<template>
  <article class="dark:bg-gray-800 grid grid-cols-12 pb-24">
    <div class="w-full col-start-1 col-span-12 grid grid-cols-12">
      <nav
        v-if="post.toc.length"
        class="
          mt-8
          col-span-2
          shadow-2xl
          rounded-lg
          p-4
          dark:bg-gray-900
          self-start
        "
      >
        <ul class="space-y-2">
          <li
            v-for="link of post.toc"
            class="dark:text-gray-600"
            :key="link.id"
          >
            <NuxtLink
              class="
                uppercase
                tracking-wider
                dark:text-gray-400
                hover:underline
              "
              :to="`#${link.id}`"
              >{{ link.text }}</NuxtLink
            >
          </li>
        </ul>
      </nav>
      <div class="col-start-4 col-span-6 w-full">
        <div>
          <h1 class="text-4xl text-center dark:text-gray-300 mt-2">
            {{ post.title }}
          </h1>
          <div class="text-center mt-1">
            <span class="text-base text-center dark:text-gray-200 mt-2">{{
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
          </div>
        </div>
        <br />
        <nuxt-content
          class="dark:text-gray-300 mt-4 prose max-w-none"
          :document="post"
        />
      </div>
    </div>
  </article>
</template>

<style lang="scss">
.nuxt-content {
  h1 {
    @apply mt-2 text-3xl font-semibold;
  }

  h2 {
    @apply mt-2 text-2xl font-semibold;
  }

  h3 {
    @apply mt-1 text-xl font-semibold;
  }

  h4 {
    @apply mt-1 text-lg font-semibold;
  }

  h5 {
    @apply mt-1 font-semibold;
    font-size: 1.1rem;
  }

  h6 {
    @apply mt-1 text-base font-semibold;
  }

  blockquote {
    @apply rounded p-2 m-2 dark:bg-gray-900 bg-gray-300;
  }

  ul {
    list-style: disc inside;
  }

  li {
    ol,
    ul {
      margin-left: 1.25rem;
    }
  }

  ol {
    list-style: decimal inside;
  }

  p {
    display: inline;
  }

  a {
    @apply text-blue-500 hover:underline;
  }

  .nuxt-content-highlight {
    pre {
      @apply rounded;
    }
  }
}
</style>
