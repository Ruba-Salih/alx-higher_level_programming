#ifndef LISTS
#define LISTS

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * struct node - doubly linked list
 * @n: integer
 * @prev: points to the previous node
 * @next: points to the next node
 *
 * Description: doubly linked list node structure
 * for Holberton project
 */

typedef dlistint_t
{
    int data;
    dlistint_t *next;
    dlistint_t *prev;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h);