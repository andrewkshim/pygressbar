#!/usr/bin/env python

import pygressbar


def main():
  limit = 1000000
  progress_bar = pygressbar.ProgressBar(limit)
  for i in range(0, limit):
    progress_bar.render()

if __name__ == "__main__":
  main()
