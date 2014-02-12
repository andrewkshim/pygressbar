"""
@author: Andrew Shim

This is a module that provides a ProgressBar object
useful for displaying the progress of long computations
on the command line.

"""
import sys

PROGRESS_BAR_WIDTH = 50 # width in terminal columns
PROGRESS_BAR_FORMAT = '\r {0:3.2%} [{1}{2}]'
COMPLETION_CHARACTER = '='
SPACE_CHARACTER = ' '

class ProgressBar(object):
  """
  This class represents an object that measures the progress
  of any long-standing computation.

  The progress bar itself has no knowledge of the measured
  computation other than a specified 'limit'; it is up to
  external methods to update the progress bar when they see
  fit.

  """

  def __init__(self, limit):
    """
    * self.limit
      Integer that denotes the amount of iterations necessary
      for the measured computation to complete.

    * self.count
      Integer that denotes how many iterations of the computation
      have completed.

    * self.percentage
      Float that denotes self.count / self.limit

    * self.bar
      String that represents the actual bar to be printed out.

    """
    self.limit = limit
    self.count = 0
    self.percentage = 0.0
    self.bar = ""

  def _calculatePercentageComplete(self):
    """
    Simple percentage calculation.
    """
    self.percentage = (self.count + 0.0) / self.limit

  def _formatProgressBar(self):
    """
    Build the output string that represents a single frame
    of the progress bar.
    """
    numberOfCompletedTicks = int(PROGRESS_BAR_WIDTH * self.percentage)
    numberOfRemainingTicks = PROGRESS_BAR_WIDTH - numberOfCompletedTicks
    self.bar = PROGRESS_BAR_FORMAT.format(
        self.percentage,
        COMPLETION_CHARACTER * numberOfCompletedTicks,
        SPACE_CHARACTER * numberOfRemainingTicks
    )

  def _tick(self):
    """
    Update progress bar parameters.
    """
    self.count += 1
    self._calculatePercentageComplete()
    self._formatProgressBar()

  def render(self):
    """
    Update progress bar and print to STDOUT.
    """
    self._tick()
    sys.stdout.write(self.bar)
    if self.count == self.limit:
      sys.stdout.write('\n')
    sys.stdout.flush()

  def reset(self):
    """
    Reset the progress bar. Use this method rather than
    creating a new progress bar.
    """
    self.count = 0

  def setLimit(self, limit):
    """
    Adjust the limit. Use this method with reset() instead
    of creating a new progress bar object.
    """
    self.limit = limit

