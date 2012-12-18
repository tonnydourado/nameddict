#! /usr/bin/env python
# -*- coding: utf8 -*-
# Tests for the nameddict module, written in konira

from nameddict import nameddict

describe "nameddict class":
    before all:
        self.class_name = "Class"

    it "accepts a name and returns a class with the given name and no parameters":
        Class = nameddict(self.class_name)
        assert Class.__name__ == self.class_name
        assert Class().__dict__ == {}

    it "accepts a list of n parameters and returns a class which takes those n parameters":
        Class = nameddict(self.class_name, ['a', 'b', 'c'])
        try:
            c = Class(1, 2, 3)
        except TypeError:
            assert False

describe "nameddict instance":
    before all:
        self.class_name = "Class"
        self.keys = ['p1', 'p2', 'p3']
        self.values = [1, 2, 3]
        for key, value in zip(self.keys, self.values):
            setattr(self, key, value)
        self.class_ = nameddict(self.class_name, self.keys)

        def assert_parameters_are_right(self, obj):
            for key, value in zip(self.keys, self.values):
                assert getattr(obj, key) == value
        self.__class__.assert_parameters_are_right = assert_parameters_are_right

    it "accepts positional parameters":
        instance = self.class_(*self.values)
        self.assert_parameters_are_right(instance)

    it "accepts named parameters":
        instance = self.class_(**dict(zip(self.keys, self.values)))
        self.assert_parameters_are_right(instance)

    it "accepts a mix of positional and named parameters":
        instance = self.class_(*self.values[:2], **dict(zip(self.keys[2:], self.values[2:])))
        self.assert_parameters_are_right(instance)

    it "can access attributes in dict notation":
        instance = self.class_(*self.values)
        for key in self.keys:
            try:
                instance[key]
            except KeyError:
                assert False

    it "can access attributes in dot notation":
        instance = self.class_(*self.values)
        assert [instance.p1, instance.p2, instance.p3] == self.values

    it "can set attributes in dict notation":
        instance = self.class_(*self.values)
        new_values = [4, 5, 6]
        for key, new_value in zip(self.keys, new_values):
            instance[key] = new_value
        assert sorted(instance.values()) == sorted(new_values)

    it "can set attributes in dot notation":
        instance = self.class_(*self.values)
        new_values = [4, 5, 6]
        instance.p1, instance.p2, instance.p3 = new_values
        assert sorted(instance.values()) == sorted(new_values)

    it "can access new attributes set with dict notation in dot notation":
        instance = self.class_(*self.values)
        new_value = 'new value!'
        instance['new'] = new_value
        assert instance.new == new_value

    it "can access new attributes set with dot notation in dict notation":
        instance = self.class_(*self.values)
        new_value = 'new value!'
        instance.new = new_value
        assert instance['new'] == new_value
