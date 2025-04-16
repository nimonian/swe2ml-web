import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Hck4ML',
  description: "The Hacker's guide to math for machine learning",
  srcDir: 'src',

  vite: {
    server: {
      port: process.env.VITE_PORT,
      strictPort: true,
      host: true,
      open: true
    }
  },

  markdown: {
    math: true,
    lineBreaks: true
  },

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Learn', link: '/learn' }
    ],

    sidebar: [
      {
        text: 'Vectors',
        collapsed: true,
        items: [
          {
            text: 'Components and dimensions',
            link: '/learn/vectors/components-and-dimensions'
          },
          {
            text: 'Adding vectors',
            link: '/learn/vectors/adding-vectors'
          },
          {
            text: 'Scaling vectors',
            link: '/learn/vectors/scaling-vectors'
          },
          {
            text: 'Vector magnitude',
            link: '/learn/vectors/vector-magnitude'
          },
          {
            text: 'Subtracting vectors',
            link: '/learn/vectors/subtracting-vectors'
          },
          {
            text: 'Unit vectors',
            link: '/learn/vectors/unit-vectors'
          },
          {
            text: 'Dot product',
            link: '/learn/vectors/dot-product'
          },
          {
            text: 'Cosine similarity',
            link: '/learn/vectors/cosine-similarity'
          },
          {
            text: 'Cross product in 2D',
            link: '/learn/vectors/cross-product-2d'
          },
          {
            text: 'Cross product in 3D',
            link: '/learn/vectors/cross-product-3d'
          },
          {
            text: 'Linear combinations',
            link: '/learn/vectors/linear-combinations'
          }
        ]
      },
      {
        text: 'Matrices',
        collapsed: true,
        items: [
          {
            text: 'Rows and columns',
            link: '/learn/matrices/rows-and-columns'
          },
          {
            text: 'Transposition',
            link: '/learn/matrices/matrix-transpose'
          },
          {
            text: 'Transforming vectors',
            link: '/learn/matrices/transforming-vectors'
          },
          {
            text: 'Special transformations',
            link: '/learn/matrices/special-transformations'
          },
          {
            text: 'Linear transformations',
            link: '/learn/matrices/linear-transformations'
          },
          {
            text: 'Matrix addition',
            link: '/learn/matrices/matrix-addition'
          },
          {
            text: 'Scaling matrices',
            link: '/learn/matrices/scaling-matrices'
          },
          {
            text: 'Matrix multiplication',
            link: '/learn/matrices/matrix-multiplication'
          },
          {
            text: 'Determinants',
            link: '/learn/matrices/determinants'
          },
          {
            text: 'Systems of equations'
          },
          {
            text: 'Inverse matrices'
          },
          {
            text: 'Change of basis'
          },
          {
            text: 'Eigenvectors'
          }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
