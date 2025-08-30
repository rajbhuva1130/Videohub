const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const Dotenv = require('dotenv-webpack');

module.exports = (env, argv) => {
  const isProduction = argv.mode === 'production';

  return {
    entry: './frontend/src/index.js',
    output: {
      filename: 'bundle.js',
      path: path.resolve(__dirname, 'backend/dist'),
      publicPath: '/',
      clean: true
    },
    devtool: isProduction ? false : 'source-map',
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: 'babel-loader'
        },
        {
          test: /\.css$/i,
          use: ['style-loader', 'css-loader']
        },
        {
          test: /\.s[ac]ss$/i,
          use: ['style-loader', 'css-loader', 'sass-loader']
        },
        {
          test: /\.(png|jpe?g|gif|svg)$/i,
          type: 'asset/resource'
        }
      ]
    },
    resolve: {
      extensions: ['.js', '.jsx']
    },
    devServer: {
      static: {
        directory: path.resolve(__dirname, 'frontend')
      },
      hot: true,
      open: true,
      port: 8001,
      watchFiles: ['frontend/**/*'],
      historyApiFallback: true,
      proxy: [
        {
          context: ['/api'],
          target: 'http://localhost:5000',
          secure: false
        }
      ]
    },
    plugins: [
      ...(isProduction
        ? [new webpack.EnvironmentPlugin(process.env)]
        : [new Dotenv()]),
      new webpack.HotModuleReplacementPlugin(),
      new HtmlWebpackPlugin({
        template: 'frontend/index.html',
        filename: 'index.html',
        inject: 'body'
      })
    ]
  };
};